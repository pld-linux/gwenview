Summary:	Simple image viewer for KDE
Summary(pl):	Prosta przegl±darka obrazków dla KDE
Name:		gwenview
Version:	1.0.0
%define	pre	pre4
Release:	0.%{pre}.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gwenview/%{name}-%{version}%{pre}.tar.bz2
# Source0-md5:	6a7ae78872f54bf87dd026b31f1ee3e5
URL:		http://gwenview.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.0
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
%setup -q -n %{name}-%{version}%{pre}

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# temporary, until glibc update
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{nb,no}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gwenview
%{_datadir}/apps/gwenview
%{_pixmapsdir}/*/*/apps/gwenview.png
%{_desktopdir}/kde/gwenview.desktop
%{_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{_mandir}/man1/*
