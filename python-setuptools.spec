# based on PLD Linux spec git://git.pld-linux.org/packages/python-setuptools.git
%define		module	setuptools
Summary:	A collection of enhancements to the Python distutils
Name:		python-setuptools
Version:	14.1.1
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
# Source0-md5:	babf06056ce4314cd4c51259582982b7
URL:		https://pypi.python.org/pypi/setuptools
BuildRequires:	python-devel
BuildArch:	noarch
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setuptools is a collection of enhancements to the Python distutils
(for Python 2.3.5 and up on most platforms; 64-bit platforms require a
minimum of Python 2.4) that allow you to more easily build and
distribute Python packages, especially ones that have dependencies on
other packages.

%package -n python3-setuptools
Summary:	A collection of enhancements to the Python distutils
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-setuptools
setuptools is a collection of enhancements to the Python distutils
(for Python 2.3.5 and up on most platforms; 64-bit platforms require a
minimum of Python 2.4) that allow you to more easily build and
distribute Python packages, especially ones that have dependencies on
other packages.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install	\
	--single-version-externally-managed	\
	--optimize 2				\
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install	\
	--single-version-externally-managed	\
	--optimize 2				\
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pkg_resources/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pkg_resources/tests

%{__rm} $RPM_BUILD_ROOT%{_bindir}/easy_install
ln -s easy_install-3.4 $RPM_BUILD_ROOT%{_bindir}/easy_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/easy_install-2.7
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/*.py[co]
%dir %{py_sitescriptdir}/_markerlib
%{py_sitescriptdir}/_markerlib/*.py[co]
%{py_sitescriptdir}/pkg_resources

%files -n python3-setuptools
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/easy_install
%attr(755,root,root) %{_bindir}/easy_install-3.4
%{py3_sitescriptdir}/%{module}*
%{py3_sitescriptdir}/__pycache__/*.py[co]
%{py3_sitescriptdir}/*.py
%{py3_sitescriptdir}/_markerlib
%{py3_sitescriptdir}/pkg_resources

