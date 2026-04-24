%define url_ver	%(echo %version | cut -d. -f 1-2)

Name:		gnome-2048
Version:	50.2
Release:	1
Summary:	A 2048 clone for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/2048
Source0:	https://download.gnome.org/sources/gnome-2048/%{url_ver}/%{name}-%{version}.tar.xz
Source1:  vendor.tar.xz

BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	libxml2-utils >= 2.15.2
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(glib-2.0) >= 2.42            
BuildRequires:  pkgconfig(gtk4)            
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  rust-packaging
Provides:       bundled(libgnome-games-support)

%description
A GNOME clone of the popular game 2048.
http://en.wikipedia.org/wiki/2048_(video_game)


%prep
%autosetup -a1 -p1
#cargo_prep -v vendor
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang 
#-f gnome-2048_libgnome-games-support.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.TwentyFortyEight.service
%{_iconsdir}/hicolor/*/apps/org.gnome.TwentyFortyEight*.*
%{_mandir}/man6/gnome-2048.6.*
