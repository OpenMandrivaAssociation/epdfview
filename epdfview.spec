Summary:	Simple and lightweight PDF viewer
Name:		epdfview
Version:	0.1.8
Release:	4
Group:		Office
License:	GPLv2+
URL:		http://trac.emma-soft.com/epdfview/
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
ePDFView is a free lightweight PDF document viewer using 
Poppler and GTK+ libraries.The aim of ePDFView is to make 
a simple PDF document viewer, in the lines of Evince but 
without using the Gnome libraries. 

%prep
%setup -q
%apply_patches

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

%files -f %{name}.lang
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/epdfview.1.*



%changelog
* Sat Jun 16 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.1.8-2
+ Revision: 806004
- Fix build in current environment

* Mon May 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.8-1
+ Revision: 681985
- update to new version 0.1.8
- drop patches3 and 4
- drop old scriplets
- fix file list

* Mon Apr 18 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-8
+ Revision: 654804
- rebuild

* Sat Apr 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-7
+ Revision: 649903
- rebuild

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 0.1.7-6mdv2011.0
+ Revision: 626174
- add patch to build with latest poppler 0.16.0
- rebuild for new poppler

* Thu Aug 05 2010 Götz Waschk <waschk@mandriva.org> 0.1.7-5mdv2011.0
+ Revision: 566236
- rebuild for new poppler

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-4mdv2010.0
+ Revision: 422601
- add requires on poppler (mdvbz #46661)
- Patch3: fox mouse scrolling (mdvbz #51414)

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 0.1.7-3mdv2010.0
+ Revision: 377482
- rebuild for new poppler

* Sat Mar 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-2mdv2009.1
+ Revision: 351898
- fix missing icon (mdvbz #48511)

* Tue Mar 03 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.7-1mdv2009.1
+ Revision: 348103
- update to the new version 0.1.7
- drop patches 0 and 1, merged upstream
- fix missing icons
- correct icon name in desktop file

* Wed Feb 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-7mdv2009.1
+ Revision: 339502
- Patch2: fix building with -Werror=format-security
- add buildrequires on bison and cppunit-devel

* Fri Jul 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-6mdv2009.0
+ Revision: 231862
- move icons to the right place
- fix icon name in menu entry
- run scriplets for mdv < 2009.0

* Sun Jun 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-5mdv2009.0
+ Revision: 219295
- Patch1: fix compilation
- rebuild for new poppler

* Fri Mar 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-4mdv2008.1
+ Revision: 190802
- Patch0: fix printing of documents, patch from upstream svn (mdv bug #39332)

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.1.6-3mdv2008.1
+ Revision: 168491
- rebuild
- fix summary

* Tue Jan 22 2008 Funda Wang <fwang@mandriva.org> 0.1.6-2mdv2008.1
+ Revision: 156326
- fix URL and tarball URL

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-1mdv2008.0
+ Revision: 83497
- Import epdfview

