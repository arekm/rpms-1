# $Id: $

# Authority: dries
# Upstream:

Summary: Small, portable symbolic math program
Name: mathomatic
Version: 11.0e
Release: 1
License: LGPL
Group: Applications/Engineering
URL: http://www.lightlink.com/computer/math/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.panix.com/~gesslein/mathomatic-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Mathomatic is a small, portable symbolic math program that can automatically
solve, simplify, differentiate, combine, and compare algebraic equations,
perform polynomial and complex arithmetic, etc. It was written by George
Gesslein II and has been under development since 1986.

%prep
%setup -n am

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 755 am %{buildroot}%{_bindir}/am
%{__install} -D -m 644 am.1 %{buildroot}%{_datadir}/man/man1/am.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/man/man1/am.*

%changelog
* Tue Apr 27 2004 Dries Verachtert <dries@ulyssis.org> 11.0e-1
- Initial package
