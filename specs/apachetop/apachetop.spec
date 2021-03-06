# $Id$
# Authority: dag
# Upstream: Chris Elsworth <chris$shagged,org>


%{!?dtag:%define _with_gamin 1}
%{?fc4:%define _with_gamin 1}
%{?el4:%define _with_gamin 1}
%{?fc3:%define _with_gamin 1}
%{?fc2:%define _with_fam 1}
%{?el3:%define _with_fam 1}

Summary: Top-like display of Apache logs
Name: apachetop
Version: 0.12.6
Release: 2%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.webta.org/projects/apachetop/wiki/Download

Source: http://www.webta.org/apachetop/apachetop-%{version}.tar.gz
Patch0: apachetop-0.12.6-gcc41.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, m4, readline-devel, gcc-c++, pcre-devel
%{?_with_gamin:BuildRequires: gamin-devel}
%{?_with_fam:BuildRequires: fam-devel}

%description
ApacheTop watches a logfile generated by Apache (in standard common or
combined logformat, although it doesn't (yet) make use of any of the extra
fields in combined) and generates human-parsable output in realtime.

%prep
%setup
%patch0

%build
%configure \
    --with-logfile="%{_localstatedir}/log/httpd/access_log"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE NEWS README TODO
%doc %{_mandir}/man1/apachetop.1*
%{_bindir}/apachetop

%changelog
* Sat Jul 28 2007 Dag Wieers <dag@wieers.com> - 0.12.6-2
- Added a patch to build on gcc 4.1. (Greg Swallow)

* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.12.6-1
- Updated to release 0.12.6.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 0.12.5-1
- Updated to release 0.12.5.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
