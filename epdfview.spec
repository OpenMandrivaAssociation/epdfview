Summary:	Simple and lightweight PDF viewer
Name:		epdfview
Version:	0.1.6
Release:	%mkrel 5
Group:		Office
License:	GPLv2+
URL:		http://trac.emma-soft.com/epdfview/
Source:		http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.1.6-fix-printing.patch
Patch1:		%{name}-0.1.6-fix-compile.patch
BuildRequires:	libpoppler-glib-devel
BuildRequires:	libcups-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
ePDFView is a free lightweight PDF document viewer using 
Poppler and GTK+ libraries.The aim of ePDFView is to make 
a simple PDF document viewer, in the lines of Evince but 
without using the Gnome libraries. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--disable-rpath \
	--with-cups
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%defattr (-,root,root)
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
