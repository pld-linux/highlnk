Summary:	Small tool to save space on read-only partitions and CDs/DVDs
Summary(pl):	Proste narzêdzie pozwalaj±ce na zaoszczêdzenie miejsca na partycjach, CDs/DVDs
Name:		highlnk
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/Console
Source0:	http://www.thpinfo.com/highlnk/%{name}-%{version}.tar.gz
# Source0-md5:	8a3364e84eac8c3f908a82951d9437b7
URL:		http://www.thpinfo.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HighLnk is a small-but-powerful tool to save space on read-only
partitions and on CDs/DVDs by hard-linking files that are the same.
You can get more onto CDs/DVDs without compression.

%description -l pl
HighLnk jest ma³ym, ale potê¿nym narzêdziem do 'oszczêdzania' miejsca
na partycjach tylko do odczytu oraz na CDs/DVDs poprzez tworzenie
twardych dowi±zañ. Daje to mo¿liwo¶æ pobrania wiêcej danych na
CDs/DVDs bez kompresji.

%prep
%setup -q

%build
%{__make}\
	 FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install highlnk $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
