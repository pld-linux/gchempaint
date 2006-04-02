Summary:	GNOME 2D chemical structure drawing tool
Summary(pl):	Program GNOME do rysowania dwuwymiarowych wzorów chemicznych
Name:		gchempaint
Version:	0.6.4
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchempaint/%{name}-%{version}.tar.bz2
# Source0-md5:	6dfe0ab484dbe997016bb0e823db8df0
URL:		http://www.nongnu.org/gchempaint/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-chemistry-utils-devel >= 0.4.7
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.1.3
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	openbabel-devel >= 1.100.2
Requires:	gnome-chemistry-utils >= 0.4.7
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

%package devel
Summary:	Header files for gchempaint
Summary(pl):	Pliki nag³ówkowe dla programu gchempaint
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}

%description devel
The gchempaint-devel package contains the header files necessary for
developing programs using gchempaint, and especially for writing new
plugins.

%description devel -l pl
Pakiet gchempaint-devel zawiera pliki nag³ówkowe niezbêdne do
tworzenia oprogramowania wykorzystuj±cego gchempaint, a zw³aszcza do
tworzenia wtyczek do niego.

%package static
Summary:	Static gchempaint libraries
Summary(pl):	Statyczne biblioteki programu gchempaint
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}

%description static
Static gchempaint libraries.

%description static -l pl
Statyczne biblioteki programu gchempaint


%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--disable-update-databases
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
/sbin/ldconfig
umask 022
update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
%scrollkeeper_update_post
/sbin/ldconfig
if [ $1 = 0 ]; then
    umask 022
    update-mime-database %{_datadir}/mime >/dev/null 2>&1
    [ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-viewer
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_datadir}/mime/packages/*
%{_desktopdir}/%{name}.desktop
%{_libdir}/bonobo/servers/%{name}.server
%{_iconsdir}/hicolor/128x128/apps/*
%{_iconsdir}/hicolor/128x128/mimetypes/*
%{_iconsdir}/hicolor/32x32/apps/*
%{_iconsdir}/hicolor/32x32/mimetypes/*
%{_iconsdir}/hicolor/48x48/apps/*
%{_iconsdir}/hicolor/48x48/mimetypes/*
%{_iconsdir}/hicolor/72x72/apps/*
%{_iconsdir}/hicolor/72x72/mimetypes/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.la
