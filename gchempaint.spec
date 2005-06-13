Summary:	GNOME 2D chemical structure drawing tool
Summary(pl):	Program GNOME do rysowania dwuwymiarowych wzorów chemicznych
Name:		gchempaint
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	6d02d5ec9b5371529b308b4ba7983a38
URL:		http://www.nongnu.org/gchempaint/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.1.3
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	gnome-chemistry-utils-devel >= 0.2.5
BuildRequires:	openbabel-devel >= 1.100.2
Requires:	gnome-chemistry-utils >= 0.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GChemPaint is a 2D chemical structures editor for the GNOME-2 desktop.
GChemPaint is a multi-document application and will be a bonobo server
so that some chemistry could be embedded in GNOME applications such as
Gnumeric and Abiword.

%description -l pl
GChemPaint jest edytorem dwuwymiarowych wzorów chemicznych dla
¶rodowiska GNOME-2. GChemPaint pozwala na edycjê wielu dokumentów
jednocze¶nie i bêdzie serwerem bonobo, co pozwoli na u¿ywanie wzorów
chemicznych w innych aplikacjach GNOME, takich jak Gnumeric czy
Abiword.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_post

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
%{_libdir}/bonobo/servers/%{name}.server
