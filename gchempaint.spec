Summary:	GNOME 2D chemical structure drawing tool
Summary(pl):	Program GNOME do rysowania dwuwymiarowych wzorów chemicznych
Name:		gchempaint
Version:	0.3.3
Release:	1
Source0:	http://savannah.nongnu.org/download/gchempaint/unstable.pkg/%{version}/%name-%{version}.tar.bz2
URL:		http://www.nongnu.org/gchempaint
License:	GPL
Group:		X11/Applications/Science
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprint-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.1.3
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	gcu-lib-devel
Requires:	gcu-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GChemPaint is a 2D chemical structures editor for the Gnome-2 desktop.
GChemPaint is a multi-document application and will be a bonobo server
so that some chemistry could be embedded in Gnome applications such as
Gnumeric and Abiword.

%description -l pl
GChemPaint jest edytorem dwuwymiarowych wzorów chemicznych dla
¶rodowiska Gnome-2. GChemPaint pozwala na edycjê wielu dokumentów
jednocze¶nie i bêdzie serwerem bonobo, co pozwoli na u¿ywanie wzorów
chemicznych w innych aplikacjach Gnome, takich jak Gnumeric czy
Abiword.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
##crappy fix for make install running scrollkeeper-update
#rm -fr $RPM_BUILD_ROOT/var

%find_lang %name


%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%name.desktop
%{_datadir}/%{name}/glade/*
%{_datadir}/gnome/*
%{_omf_dest_dir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/mime-info/%{name}.*
%{_libdir}/bonobo/servers/%{name}.server
