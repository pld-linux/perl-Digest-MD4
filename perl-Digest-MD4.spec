%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	MD4
Summary:	Digest::MD4 Perl module - MD4 digest algorithm implementation
Summary(pl):	Modu³ perla Digest::MD4 - implementacja algorytmu skrótu MD4
Name:		perl-Digest-MD4
Version:	1.1
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::MD4 module allows you to use the RSA Data Security Inc.
MD4 Message Digest algorithm from within Perl programs. The algorithm
is described in RFC 1320.

%description -l pl
Modu³ Digest::MD4 pozwala na u¿ywanie algorytmu skrótu MD4 firmy RSA
Data Security Inc. w programach perlowych. Algorytm jest opisany w RFC
1320.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Digest/MD4.pm
%dir %{perl_sitearch}/auto/Digest/MD4
%{perl_sitearch}/auto/Digest/MD4/autosplit.ix
%{perl_sitearch}/auto/Digest/MD4/MD4.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/MD4/MD4.so
%{_mandir}/man3/*
