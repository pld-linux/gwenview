Summary:	Simple image viewer for KDE
Summary(pl):	Prosta przegl±darka obrazków dla KDE
Name:		gwenview
Version:	1.0.1
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gwenview/%{name}-%{version}.tar.bz2
# Source0-md5:	98bc89e3bda282cf192f84bd1fc03fdf
URL:		http://gwenview.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	sed >= 4.0
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

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# temporary, until glibc update
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{nb,no}

sed -i 's/Categories=Qt;KDE;Graphics/&;Viewer/' \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/gwenview.desktop


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gwenview
%{_datadir}/apps/gwenview
%{_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{_desktopdir}/kde/gwenview.desktop
%{_iconsdir}/[!l]*/*/apps/gwenview.png
%{_mandir}/man1/*
