Summary:	GNOME 2D chemical structure drawing tool
Summary(pl.UTF-8):   Program GNOME do rysowania dwuwymiarowych wzorów chemicznych
Name:		gchempaint
Version:	0.6.4
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchempaint/%{name}-%{version}.tar.bz2
# Source0-md5:	6dfe0ab484dbe997016bb0e823db8df0
URL:		http://www.nongnu.org/gchempaint/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gnome-chemistry-utils-devel >= 0.4.7
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libbonoboui-devel >= 2.6.0
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	shared-mime-info >= 0.12
BuildRequires:	which
Requires(post,postun):	scrollkeeper
Requires(post,postun):	/sbin/ldconfig
Requires:	gnome-chemistry-utils >= 0.4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GChemPaint is a 2D chemical structures editor for the GNOME-2 desktop.
GChemPaint is a multi-document application and will be a bonobo server
so that some chemistry could be embedded in GNOME applications such as
Gnumeric and Abiword.

%description -l pl.UTF-8
GChemPaint jest edytorem dwuwymiarowych wzorów chemicznych dla
środowiska GNOME-2. GChemPaint pozwala na edycję wielu dokumentów
jednocześnie i będzie serwerem bonobo, co pozwoli na używanie wzorów
chemicznych w innych aplikacjach GNOME, takich jak Gnumeric czy
Abiword.

%package devel
Summary:	Header files for gchempaint
Summary(pl.UTF-8):   Pliki nagłówkowe dla programu gchempaint
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-chemistry-utils-devel >= 0.4.7
Requires:	gnome-vfs2-devel >= 2.6.0
Requires:	gtk+2-devel >= 2:2.6.0
Requires:	libbonoboui-devel >= 2.6.0
Requires:	libglade2-devel >= 2.4.0
Requires:	libgnomeprintui-devel >= 2.6.0
Requires:	libgnomeui-devel >= 2.6.0

%description devel
The gchempaint-devel package contains the header files necessary for
developing programs using gchempaint, and especially for writing new
plugins.

%description devel -l pl.UTF-8
Pakiet gchempaint-devel zawiera pliki nagłówkowe niezbędne do
tworzenia oprogramowania wykorzystującego gchempaint, a zwłaszcza do
tworzenia wtyczek do niego.

%package static
Summary:	Static gchempaint libraries
Summary(pl.UTF-8):   Statyczne biblioteki programu gchempaint
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gchempaint libraries.

%description static -l pl.UTF-8
Statyczne biblioteki programu gchempaint.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-update-databases \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{la,a}

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
%scrollkeeper_update_postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	umask 022
	update-mime-database %{_datadir}/mime >/dev/null 2>&1
	[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-viewer
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%{_libdir}/bonobo/servers/%{name}.server
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_datadir}/mime/packages/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/128x128/apps/*
%{_iconsdir}/hicolor/128x128/mimetypes/*
%{_iconsdir}/hicolor/32x32/apps/*
%{_iconsdir}/hicolor/32x32/mimetypes/*
%{_iconsdir}/hicolor/48x48/apps/*
%{_iconsdir}/hicolor/48x48/mimetypes/*
%{_iconsdir}/hicolor/72x72/apps/*
%{_iconsdir}/hicolor/72x72/mimetypes/*
%{_omf_dest_dir}/gchempaint

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
