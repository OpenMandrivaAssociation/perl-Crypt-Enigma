%define real_name Crypt-Enigma

Summary:	Crypt-Enigma module for perl 
Name:		perl-%{real_name}
Version:	1.3
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
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


