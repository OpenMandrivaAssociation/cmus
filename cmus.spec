%global _disable_ld_no_undefined 1

# Pick git head and avoid to have too many patches
%define	gitcommit	56446f70e86445caa96f6f4f0188f175fc1fd9a0
%define	gitdate	20251212

Summary:	A powerful ncurses-based music player
Name:	cmus
Version:	2.12.0
Release:	4
License:	GPLv2+
Group:	Sound
Url:		https://cmus.github.io/
%if %{gitdate}
Source0:	%{name}-%{gitdate}.tar.xz
%else
Source0:	https://github.com/cmus/cmus/archive/%{name}-%{version}.tar.gz
%endif
Patch0:	cmus-20251007-fix-install.patch
BuildRequires:	libmp4v2-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio_cdda)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libmikmod)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndio)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(vorbisenc)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(wavpack)
Requires:	ncurses

%description
Cmus is a powerful music player with an ncurses UI. It supports many
different file types like FLAC, Ogg/Vorbis, etc. and is able to handle play
lists.

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/ip/
%dir %{_libdir}/%{name}/op/
%{_libdir}/%{name}/*/*.so
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.theme
%{_datadir}/%{name}/rc
%{_datadir}/bash-completion/completions/%{name}
%{_docdir}/%{name}/examples/%{name}-status-display
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-remote.1*
%{_mandir}/man7/%{name}-tutorial.7*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{gitdate}


%build
# Not an autotools configure: we cannot use our macro
%set_build_flags
./configure \
	prefix="%{_prefix}" \
	libdir="%{_libdir}" \
	bindir="%{_bindir}" \
	mandir="%{_mandir}" \
	CONFIG_MIKMOD=y \
	CONFIG_ROAR=n \
	DEBUG=0

%make_build all


%install
%make_install

# Install the not automatically installed completion files
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -m644 contrib/%{name}.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
