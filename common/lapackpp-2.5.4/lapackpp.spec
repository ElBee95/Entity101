# norootforbuild
# neededforbuild gcc gcc-c++ gcc-fortran lapack blas

%define name lapackpp

%define is_mandrake %(test -e /etc/mandrake-release && echo 1 || echo 0)
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)
%define is_fedora %(test -e /etc/fedora-release && echo 1 || echo 0)

%define dist redhat
%define disttag rh

%if %is_mandrake
%define dist mandrake
%define disttag mdk
%endif
%if %is_suse
%define dist suse
%define disttag suse
%endif
%if %is_fedora
%define dist fedora
%define disttag rhfc
%endif
#
%define version 2.5.4

%define distver %(release="`rpm -q --queryformat='%{VERSION}' %{dist}-release 2>/dev/null`" ; if test $? != 0 ; then release="" ; fi ; echo "$release")

%define release 1.%{disttag}%{distver}

Name: %{name}
Summary: A library for high performance linear algebra computations.
Version: %{version}
Release: %{release}
Source: http://download.sourceforge.net/lapackpp/%{name}-%{version}.tar.gz
Group: System Environment/Libraries
License: LGPL
Packager: Christian Stimming <stimming@tuhh.de>
URL: http://www.sourceforge.net/projects/lapackpp
BuildRoot: %{_tmppath}/%{name}-%{version}-root
# in case it gets split sometime
Provides: %{name}-devel = %{version}-%{release}
Prereq: /sbin/ldconfig
Prefix: %{_prefix}

%description 
LAPACK++ is a library for high performance linear algebra computations.
This version includes support for solving linear systems using LU, Cholesky,
QR matrix factorizations, and symmetric eigenvalue problems.

%prep
%setup -q

%build
%{configure}
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README MAINTAINER COPYING NEWS ChangeLog
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/lapackpp.pc
%{_includedir}/lapackpp
%{_datadir}/aclocal/acx_lapackpp.m4

%changelog
