
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define pnam	ACL
Summary:	Net::ACL - Class representing a generic access-list/route-map
Name:		perl-Net-ACL
Version:	0.07
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	351d7ef33c2c44ccab2911cef33b8a51
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Net::Netmask)
BuildRequires:	perl(Cisco::Reconfig)
BuildRequires:	perl(Test::Signature)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::ACL module allows a Perl program to do complex filtering and
manipulation of data in the same way as routers does with access-lists
and route-maps.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Net/ACL.pm
%dir %{perl_vendorlib}/Net/ACL
%{perl_vendorlib}/Net/ACL/*.pm
%dir %{perl_vendorlib}/Net/ACL/File
%{perl_vendorlib}/Net/ACL/File/*.pm
%dir %{perl_vendorlib}/Net/ACL/Match
%{perl_vendorlib}/Net/ACL/Match/*.pm
%dir %{perl_vendorlib}/Net/ACL/Set
%{perl_vendorlib}/Net/ACL/Set/*.pm
%{_mandir}/man3/*
