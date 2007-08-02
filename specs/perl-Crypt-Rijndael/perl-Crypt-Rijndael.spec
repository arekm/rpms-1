# $Id$
# Authority: dries
# Upstream: Rafael R. Sevilla <sevillar$team,ph,inter,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Rijndael

Summary: Crypt::CBC compliant Rijndael encryption module
Name: perl-Crypt-Rijndael
Version: 1.04
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Rijndael/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Rijndael-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is Crypt::Rijndael, an XS-based implementation of the newly-selected
Advanced Encryption Standard algorithm Rijndael, designed by Joan Daemen
and Vincent Rijmen.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes LICENSE MANIFEST META.yml NEWS README
%doc %{_mandir}/man3/Crypt::Rijndael.3*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Rijndael.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Rijndael/

%changelog
* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
