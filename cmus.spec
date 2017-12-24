%define _disable_ld_no_undefined 1

Name:		cmus
Version:	2.7.1
Release:	1
Summary:	A powerful ncurses-based music player
URL:		http://cmus.github.io/
License:	GPLv2
Source:		https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
Patch0:		cmus-2.7.1-fix-install.patch
BuildRequires:	ffmpeg-devel
BuildRequires:	libmp4v2-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libcdio_cdda)

Requires:	ncurses

%description
cmus is a powerful music player with an ncurses UI. It supports many
different file types like FLAC, Ogg/Vorbis, etc. and is able to handle play
lists.
%if "%{?distro_section}" == "tainted"
This package is in the "tainted" section as it requires other "tainted" packages.
%endif

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
./configure prefix=%{_prefix} libdir=%{_libdir} DEBUG=0
%make

%install
%makeinstall_std

%files
%doc README.md
%{_bindir}/*
%{_libdir}/cmus/
%{_datadir}/cmus/
%{_mandir}/man1/*
%{_mandir}/man7/*
