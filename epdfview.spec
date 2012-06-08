Summary:	Simple and lightweight PDF viewer
Name:		epdfview
Version:	0.1.8
Release:	2
Group:		Office
License:	GPLv2+
URL:		http://trac.emma-soft.com/epdfview/
Source:		http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.bz2
Patch1:		epdfview-0.1.8-compile.patch
Patch2:		epdfview-0.1.6-format_not_a_string_literal_and_no_format_arguments.patch
BuildRequires:	libpoppler-glib-devel
BuildRequires:	cups-devel
BuildRequires:	bison
BuildRequires:	cppunit-devel
Requires:	poppler
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
ePDFView is a free lightweight PDF document viewer using 
Poppler and GTK+ libraries.The aim of ePDFView is to make 
a simple PDF document viewer, in the lines of Evince but 
without using the Gnome libraries. 

%prep
%setup -q
%patch1 -p1 -b .compile~
%patch2 -p1

%build
%configure2_5x \
	--disable-rpath \
	--with-cups
%make

%install
rm -fr %buildroot
%makeinstall_std

# (tpg) move icons to the right place
for i in 24 32 48;do
mkdir -p %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps
cp %{buildroot}%{_datadir}/%{name}/pixmaps/icon_epdfview-$i.png %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps/%{name}.png;
done

sed -i -e 's/^Icon=icon_epdfview-48$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/epdfview.1.*
