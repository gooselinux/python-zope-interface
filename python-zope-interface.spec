%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		python-zope-interface
Version:	3.5.2
Release:	2.1%{?dist}
Summary:	Zope 3 Interface Infrastructure
Group:		Development/Libraries
License:	ZPLv2.1
URL:		http://pypi.python.org/pypi/zope.interface
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
Source1:	ZPL-2.1.txt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	python-devel
# zope.interface 3.5.0 won't build the C extension if distutils are used
BuildRequires:  python-setuptools-devel
Requires:       python-zope-filesystem

%description
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%prep
%setup -n zope.interface-%{version} -q
%{__cp} -a %{SOURCE1} .

# Tests require additional modules and shouldn't be packaged
%{__rm} -rfv src/zope/interface/tests/
%{__rm} -rfv src/zope/interface/common/tests/

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root  %{buildroot}

# Will put docs in %{_docdir} instead
%{__rm} -f %{buildroot}%{python_sitearch}/zope/interface/*.txt

# C files don't need to be packaged
%{__rm} -f %{buildroot}%{python_sitearch}/zope/interface/_zope_interface_coptimizations.c

# Fix permissions of shared objects to placate rpmlint
%{__chmod} 755  %{buildroot}%{python_sitearch}/zope/interface/_zope_interface_coptimizations.so

%check
# Skipped; would require zope.testing, which isn't in Fedora yet

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ZPL-2.1.txt src/zope/interface/*.txt
%{python_sitearch}/zope/*
%{python_sitearch}/zope.interface*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.5.2-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.2-1
- update to 3.5.2

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> 3.5.1-3
- Add python-setuptools-devel to the BuildRequires, so we generate egg-info

* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.1-2
- use correct source filename (upstream switched from zip to tar.gz)

* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.1-1
- update to 3.5.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 3.5.0-3
- Make compatible with the new python-zope-filesystem.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.5.0-2
- Rebuild for Python 2.6

* Sat Nov 15 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 3.5.0-1
- update to 3.5.0

* Mon Mar 31 2008 Paul Howarth <paul@city-fan.org> 3.4.1-1
- update to 3.4.1
- incorporate suggestions from Felix Schwarz:
  - new summary and description
  - new upstream URL (old one out of date)
  - don't package test files
  - include more documentation

* Mon Mar 31 2008 Paul Howarth <paul@city-fan.org> 3.3.0-1
- update to 3.3.0
- update source URL to include versioned directory and new tarball name
- drop the gcc 4.x compatibility patch, no longer needed
- don't run the test suite as it now depends on zope.testing
- exclude _zope_interface_coptimizations.c source from the binary package

* Thu Feb 14 2008 Paul Howarth <paul@city-fan.org> 3.0.1-10
- rebuild with gcc 4.3.0 for Fedora 9

* Fri Jan  4 2008 Paul Howarth <paul@city-fan.org> 3.0.1-9
- tweak %%files list to pull in egg info file when necessary
- fix permissions on shared objects (silence rpmlint)

* Wed Aug 29 2007 Paul Howarth <paul@city-fan.org> 3.0.1-8
- update license tag to ZPLv2.1 in anticipation of this tag being approved

* Sat Dec  9 2006 Paul Howarth <paul@city-fan.org> 3.0.1-7
- rebuild against python 2.5 for Rawhide

* Tue Oct 31 2006 Paul Howarth <paul@city-fan.org> 3.0.1-6
- add %%check section

* Wed Sep 20 2006 Paul Howarth <paul@city-fan.org> 3.0.1-5
- dispense with %%{pybasever} macro and python-abi dependency, not needed from
  FC4 onwards
- include ZPL 2.1 license text
- add reference in %%description to origin of patch
- change License: tag from "ZPL 2.1" to "Zope Public License" to shut rpmlint up

* Thu Aug 31 2006 Paul Howarth <paul@city-fan.org> 3.0.1-4
- files list simplified as .pyo files are no longer %%ghost-ed

* Tue May  9 2006 Paul Howarth <paul@city-fan.org> 3.0.1-3
- import from PyVault Repository
- rewrite in Fedora Extras style

* Tue Aug 23 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 3.0.1-2
- add bug fix for gcc 4

* Mon Feb 07 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 3.0.1-1
- new rpm

