%define	_disable_ld_no_undefined 0

Summary:	A powerful ncurses-based music player
Name:		cmus
Version:	2.8.0
Release:	1.rc0
License:	GPLv2+
Group:		Sound
Url:		https://cmus.github.io/
Source0:	https://github.com/cmus/cmus/archive/%{name}-%{version}-rc0.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	ffmpeg-devel
BuildRequires:	libmp4v2-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	soundio-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(flac)
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
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(vorbis)
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
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-remote.1*
%{_mandir}/man7/%{name}-tutorial.7*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-rc0


%build
%setup_compile_flags
./configure \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	CONFIG_MIKMOD=y \
	DEBUG=0
%make


%install
%makeinstall_std

