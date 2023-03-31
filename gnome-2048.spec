%define url_ver	%(echo %version | cut -d. -f 1-2)

Name:		gnome-2048
Version:	3.38.2
Release:	5
Summary:	A 2048 clone for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/2048
Source0:	https://download.gnome.org/sources/gnome-2048/%{url_ver}/%{name}-%{version}.tar.xz

# Merge request (not yet merged) for fix compilation with Meson 0.60+
Patch0:   https://gitlab.gnome.org/GNOME/gnome-2048/-/merge_requests/21.patch

BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(libgnome-games-support-1)

%description
A GNOME clone of the popular game 2048.
http://en.wikipedia.org/wiki/2048_(video_game)


%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.appdata.xml
%{_iconsdir}/hicolor/*/apps/org.gnome.TwentyFortyEight*.*
%{_mandir}/man6/gnome-2048.6.*
