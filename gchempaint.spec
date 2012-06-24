Summary:	GNOME 2D chemical structure drawing tool
Summary(pl):	Program GNOME do rysowania dwuwymiarowych wzor�w chemicznych
Name:		gchempaint
Version:	0.3.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchempaint/unstable.pkg/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	cdf5fa5d07884a1ee6a00cf6acb40ed8
URL:		http://www.nongnu.org/gchempaint/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprint-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.1.3
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	gnome-chemistry-utils-devel >= 0.1.3
Requires:	gnome-chemistry-utils >= 0.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GChemPaint is a 2D chemical structures editor for the GNOME-2 desktop.
GChemPaint is a multi-document application and will be a bonobo server
so that some chemistry could be embedded in GNOME applications such as
Gnumeric and Abiword.

%description -l pl
GChemPaint jest edytorem dwuwymiarowych wzor�w chemicznych dla
�rodowiska GNOME-2. GChemPaint pozwala na edycj� wielu dokument�w
jednocze�nie i b�dzie serwerem bonobo, co pozwoli na u�ywanie wzor�w
chemicznych w innych aplikacjach GNOME, takich jak Gnumeric czy
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
# it seems to be the only package using this dir
%dir %{_datadir}/gnome/ui
%{_datadir}/gnome/ui/*.xml
%{_omf_dest_dir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
%{_datadir}/mime-info/%{name}.*
%{_libdir}/bonobo/servers/%{name}.server
