Summary:	Textmode web browser
Summary(pl):	Tekstowa przegl±darka WWW
Name:		retawq
Version:	0.2.5a
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/retawq/%{name}-%{version}.tar.gz
# Source0-md5:	5db8e54c8e54526a4cc7b14494e0ea7c
URL:		http://retawq.sourceforge.net/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
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

%description -l pl
retawq jest interaktywnym, wielow±tkowym klientem sieciowym 
(przegl±dark± WWW) dla tekstowych terminali na systemach 
Uniksopodobnych. Jest napisany w C, szybki, ma³y, konfigurowalny i 
komfortowy. Przyk³adowo: niskopoziomowa komunikacja sieciowa jest 
wykonywana w sposób nie blokuj±cy, mo¿esz otworzyæ tyle "wirtualnych 
okien" ile zechcesz i pracowaæ jednocze¶nie z dwoma z nich w trybie
dzielenia ekranu.

%prep
%setup -q

%build
./configure CFLAGS="%{rpmcflags} %{rpmldflags} -I/usr/include/ncurses" \
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
%doc INSTALL README docu/{*.html,example*}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
