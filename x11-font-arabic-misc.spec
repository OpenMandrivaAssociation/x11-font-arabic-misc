Name: x11-font-arabic-misc
Version: 1.0.3
Release: 13
Summary: Xorg X11 font arabic-misc
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-arabic-misc-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale
Conflicts: xorg-x11 <= 6.9.0

%description
Xorg X11 font arabic-misc

%prep
%setup -q -n font-arabic-misc-%{version}

%build
%configure --with-fontdir=%_datadir/fonts/misc
%make

%install
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/misc/fonts.dir
rm -f %{buildroot}%_datadir/fonts/misc/fonts.scale

%post
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%postun
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%files
%doc COPYING
%_datadir/fonts/misc/arabic24.pcf.gz
