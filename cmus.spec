%global _disable_ld_no_undefined 1

Summary:	A powerful ncurses-based music player
Name:	cmus
Version:	2.12.0
Release:	2
License:	GPLv2+
Group:		Sound
Url:		https://cmus.github.io/
Source0:	https://github.com/cmus/cmus/archive/%{name}-%{version}.tar.gz
Patch0:	cmus-2.12.0-fix-install.patch
Patch1:	cmus-2.12.0-ensure-the-buffer-is-at-least-80ms.patch
Patch2:	cmus-2.12.0-make-the-buffer-capacity-configurable.patch
Patch3:	cmus-2.12.0-check-for-libavutil.patch
Patch4:	cmus-2.12.0-add-sort-by-duration.patch
Patch5:	cmus-2.12.0-respect-scroll_offset-when-resizing-window.patch
Patch6:	cmus-2.12.0-try-to-fallback-upon-plugin-output-init-failure.patch
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
%autosetup -p1


%build
# Not an autotools configure: we cannot use our macro
%set_build_flags
./configure \
	prefix="%{_prefix}" \
	libdir="%{_libdir}" \
	bindir="%{_bindir}" \
	mandir="%{_mandir}" \
	CONFIG_MIKMOD=y \
	DEBUG=0

%make_build


%install
%make_install

# Install the not automatically installed completion files
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -m644 contrib/%{name}.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
