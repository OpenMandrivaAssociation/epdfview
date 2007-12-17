Summary:	ePDFView is a simple and lightweight PDF viewer
Name:		epdfview
Version:	0.1.6
Release:	%mkrel 1
Group:		Office
License:	GPL
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	libpoppler-glib-devel
BuildRequires:	libcups-devel

%description
ePDFView is a free lightweight PDF document viewer using 
Poppler and GTK+ libraries.The aim of ePDFView is to make 
a simple PDF document viewer, in the lines of Evince but 
without using the Gnome libraries. 

%prep
%setup -q

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
