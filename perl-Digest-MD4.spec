#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Digest
%define	pnam	MD4
Summary:	Digest::MD4 - MD4 digest algorithm implementation
Summary(pl):	Digest::MD4 - implementacja algorytmu skrótu MD4
Name:		perl-Digest-MD4
Version:	1.4
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	20475bab07a6ca98e6812ff9c555149c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::MD4 module allows you to use the RSA Data Security Inc.
MD4 Message Digest algorithm from within Perl programs.  The algorithm
is described in RFC 1320.

%description -l pl
Modu³ Digest::MD4 pozwala na u¿ywanie algorytmu skrótu MD4 firmy RSA
Data Security Inc. w programach perlowych. Algorytm jest opisany w RFC
1320.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Digest/MD4.pm
%dir %{perl_vendorarch}/auto/Digest/MD4
%{perl_vendorarch}/auto/Digest/MD4/MD4.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/MD4/MD4.so
%{_mandir}/man3/*
