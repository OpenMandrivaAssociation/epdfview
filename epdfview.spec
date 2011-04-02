Summary:	Simple and lightweight PDF viewer
Name:		epdfview
Version:	0.1.7
Release:	%mkrel 7
Group:		Office
License:	GPLv2+
URL:		http://trac.emma-soft.com/epdfview/
Source:		http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.bz2
Patch2:		epdfview-0.1.6-format_not_a_string_literal_and_no_format_arguments.patch
# (tpg) https://qa.mandriva.com/show_bug.cgi?id=51414
Patch3:		epdfview-0.1.7-fix-mouse-scroll.patch
Patch4:		epdfview-0.1.7-poppler-0.16.0.patch
BuildRequires:	libpoppler-glib-devel
BuildRequires:	libcups-devel
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
%patch2 -p1
%patch4 -p0

%build
touch ChangeLog
autoreconf -fi
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

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr (-,root,root)
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*
