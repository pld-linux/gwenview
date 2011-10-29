%define		_state		stable
%define		orgname		gwenview
%define		qtver		4.7.4

Summary:	K Desktop Environment - Simple image viewer
Summary(pl.UTF-8):	K Desktop Environment - Prosta przeglądarka obrazków
Name:		gwenview
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	71809b5736992a912aa7032adba2f615
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libkipi-devel >= %{version}
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
Obsoletes:	kde4-kdegraphics-gwenview < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide
easy navigation in your file hierarchy. Image loading is done by the
Qt library, so it supports all image formats your Qt installation
supports.

%description -l pl.UTF-8
Gwenview to przeglądarka obrazków dla KDE. Ma okno z drzewem katalogów
oraz okno z listą plików w celu zapewnienia łatwej nawigacji w
hierarchii plików. Wczytywanie obrazków jest wykonywane przez
bibliotekę Qt, więc przeglądarka obsługuje wszystkie formaty
obsługiwane przez zainstalowaną wersję Qt.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenview
%attr(755,root,root) %{_bindir}/gwenview_importer
%attr(755,root,root) %{_libdir}/libgwenviewlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwenviewlib.so.?
%attr(755,root,root) %{_libdir}/kde4/gvpart.so
%dir %{_datadir}/apps/gwenview
%dir %{_datadir}/apps/gwenview/cursors
%{_datadir}/apps/gwenview/cursors/zoom.png
%{_datadir}/apps/gwenview/fullscreenthemes
%{_datadir}/apps/gwenview/gwenviewui.rc
%dir %{_datadir}/apps/gvpart
%{_datadir}/apps/gvpart/gvpart.rc
%{_datadir}/kde4/services/gvpart.desktop
%{_datadir}/kde4/services/ServiceMenus/slideshow.desktop
%{_desktopdir}/kde4/gwenview.desktop
%{_datadir}/apps/solid/actions/gwenview_importer.desktop
%{_datadir}/apps/solid/actions/gwenview_importer_camera.desktop
%{_iconsdir}/*/*/actions/document-share.png
%{_iconsdir}/*/*/apps/gwenview.png
%{_iconsdir}/*/scalable/apps/gwenview.svgz
%{_iconsdir}/*/scalable/actions/document-share.svgz
%{_kdedocdir}/en/gwenview
