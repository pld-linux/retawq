Summary:	Textmode web browser
Summary(pl.UTF-8):	Tekstowa przeglądarka WWW
Name:		retawq
Version:	0.2.6c
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/retawq/%{name}-%{version}.tar.gz
# Source0-md5:	ee60188bea597680bd39e435a8c73ff9
URL:		http://retawq.sourceforge.net/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
retawq is an interactive, multi-threaded network client (web browser)
for text terminals on computers with Unix-like operating systems. It
is written in C, fast, small, nicely configurable, and comfortable;
e.g. the low-level network communications are performed in a
non-blocking way, and you can keep open as many "virtual windows" as
you want and work simultaneously in two of them in a split-screen
mode.

%description -l pl.UTF-8
retawq jest interaktywnym, wielowątkowym klientem sieciowym
(przeglądarką WWW) dla tekstowych terminali na systemach
uniksopodobnych. Jest napisany w C, szybki, mały, konfigurowalny i
komfortowy. Przykładowo: niskopoziomowa komunikacja sieciowa jest
wykonywana w sposób nie blokujący, możesz otworzyć tyle "wirtualnych
okien" ile zechcesz i pracować jednocześnie z dwoma z nich w trybie
dzielenia ekranu.

%prep
%setup -q

%build
./configure \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags} -I/usr/include/ncurses" \
	--path-prefix=$RPM_BUILD_ROOT%{_prefix} \
	--path-man=$RPM_BUILD_ROOT%{_mandir} \
	--enable-textmodemouse \
	--enable-i18n \
	--enable-local-cgi \
	--enable-ipv6 \
	--set-tls=2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docu/{*.html,example*}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
