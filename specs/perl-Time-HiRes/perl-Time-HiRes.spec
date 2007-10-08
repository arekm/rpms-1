# $Id$
# Authority: dag
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-HiRes

Summary: Perl module that implements high resolution alarm, sleep, gettimeofday, interval timers
Name: perl-Time-HiRes
Version: 1.9707
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-HiRes/

Source: http://www.cpan.org/modules/by-module/Time/Time-HiRes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Time-HiRes is a Perl module that implements high resolution alarm,
sleep, gettimeofday, interval timers.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Time::HiRes.3pm*
%dir %{perl_vendorarch}/Time/
%{perl_vendorarch}/Time/HiRes.pm
%dir %{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/auto/Time/HiRes/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.9707-1
- Initial package. (using DAR)
