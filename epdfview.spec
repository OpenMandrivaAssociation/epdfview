Summary:	Simple and lightweight PDF viewer
Name:		epdfview
Version:	0.1.8
Release:	6
License:	GPLv2+
Group:		Office
Url:		https://trac.emma-soft.com/epdfview/
Source0:	http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.bz2
Patch1:		epdfview-0.1.8_glibh.patch
Patch2:		epdfview-0.1.6-format_not_a_string_literal_and_no_format_arguments.patch
Patch3:		epdfview-0.1.8-bgra_to_rgba.patch
Patch4:		epdfview-0.1.8-cups-1.6.patch
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(poppler-glib)
Requires:	poppler

%description
ePDFView is a free lightweight PDF document viewer using Poppler and GTK+
libraries.The aim of ePDFView is to make a simple PDF document viewer,
in the lines of Evince but without using the Gnome libraries.

%files -f %{name}.lang
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/epdfview.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x \
	--disable-rpath \
	--with-cups
%make

%install
%makeinstall_std

# (tpg) move icons to the right place
for i in 24 32 48;do
mkdir -p %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps
cp %{buildroot}%{_datadir}/%{name}/pixmaps/icon_epdfview-$i.png %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps/%{name}.png;
done

sed -i -e 's/^Icon=icon_epdfview-48$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

