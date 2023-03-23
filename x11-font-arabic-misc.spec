Name: x11-font-arabic-misc
Version: 1.0.4
Release: 1
Summary: Xorg X11 font arabic-misc
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-arabic-misc-%{version}.tar.xz
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font arabic-misc.

%prep
%autosetup -p1 -n font-arabic-misc-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/misc
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.scale

%post
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%postun
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%files
%doc COPYING
%{_datadir}/fonts/misc/arabic24.pcf.gz
