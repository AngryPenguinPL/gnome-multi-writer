%define url_ver %(echo %{version}|cut -d. -f1,2)
%define busname org.gnome.MultiWriter

Name:		gnome-multi-writer
Version:	3.30.0
Release:	1
Summary:	Write and verify an ISO file to up to 20 USB devices at once
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/MultiWriter
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.11.2
BuildRequires:	pkgconfig(udisks2)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(gusb) >= 0.2.2
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	appstream-util
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
BuildRequires:	meson
Requires:	gsettings-desktop-schemas

%description
GNOME MultiWriter allows to write and verify an ISO file to up to 20 USB
devices at once.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/gnome-multi-writer-probe
%{_datadir}/applications/%{busname}.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/metainfo/%{busname}.appdata.xml
%{_datadir}/polkit-1/actions/%{busname}.policy
%{_mandir}//man1/%{name}.1*
%{_iconsdir}/*/*/*/*.*
