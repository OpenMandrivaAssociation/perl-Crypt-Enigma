%define real_name Crypt-Enigma

Summary:	Crypt-Enigma module for perl 
Name:		perl-%{real_name}
Version:	1.3
Release:	7
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a Perl implementation of the WWII Enigma Machine

%prep
%setup -q -n %{real_name}-%{version} 
chmod 0644 examples/*.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples
%{perl_vendorlib}/Crypt/Enigma.pm
%{_mandir}/*/*




%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.3-5mdv2011.0
+ Revision: 680851
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2011.0
+ Revision: 430352
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 256262
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.3-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- initial Mandriva package

