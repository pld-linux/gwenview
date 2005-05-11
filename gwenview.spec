Summary:	Simple image viewer for KDE
Summary(pl):	Prosta przegl±darka obrazków dla KDE
Name:		gwenview
Version:	1.1.8
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gwenview/%{name}-%{version}.tar.bz2
# Source0-md5:	f2c7a984274b8010da25ad20ef62db5a
Patch0:		%{name}-pl.po.patch
URL:		http://gwenview.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040511
Requires:	kdebase-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide
easy navigation in your file hierarchy. Image loading is done by the
Qt library, so it supports all image formats your Qt installation
supports.

%description -l pl
Gwenview to przegl±darka obrazków dla KDE. Ma okno z drzewem katalogów
oraz okno z list± plików w celu zapewnienia ³atwej nawigacji w
hierarchii plików. Wczytywanie obrazków jest wykonywane przez
bibliotekê Qt, wiêc przegl±darka obs³uguje wszystkie formaty
obs³ugiwane przez zainstalowan± wersjê Qt.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

sed -i 's/Categories=.*/Categories=Qt;KDE;Graphics;Viewer;/' \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/gwenview.desktop

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/ve{n,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gwenview
%{_libdir}/libgwenviewcore.la
%attr(755,root,root) %{_libdir}/libgwenviewcore.so
%attr(755,root,root) %{_libdir}/libgwenviewcore.so.*.*.*
%{_libdir}/kde3/libgvdirpart.la
%attr(755,root,root) %{_libdir}/kde3/libgvimagepart.so
%{_libdir}/kde3/libgvimagepart.la
%attr(755,root,root) %{_libdir}/kde3/libgvdirpart.so
%{_datadir}/apps/gvdirpart
%{_datadir}/apps/gvimagepart
%{_datadir}/apps/gwenview
%{_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{_datadir}/services/gvdirpart.desktop
%{_datadir}/services/gvimagepart.desktop
%{_desktopdir}/kde/gwenview.desktop
%{_iconsdir}/[!l]*/*/apps/gwenview.png
%{_iconsdir}/[!l]*/*/apps/imagegallery.png
%{_mandir}/man1/*
