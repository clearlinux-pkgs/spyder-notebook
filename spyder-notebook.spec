#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spyder-notebook
Version  : 0.2.2
Release  : 20
URL      : https://files.pythonhosted.org/packages/a6/be/36e6db95eab4cf9f4f024cfd87d44216a445b29eccc8b526982e316ddded/spyder-notebook-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/be/36e6db95eab4cf9f4f024cfd87d44216a445b29eccc8b526982e316ddded/spyder-notebook-0.2.2.tar.gz
Summary  : Jupyter notebook integration with Spyder
Group    : Development/Tools
License  : MIT
Requires: spyder-notebook-license = %{version}-%{release}
Requires: spyder-notebook-python = %{version}-%{release}
Requires: spyder-notebook-python3 = %{version}-%{release}
Requires: QtPy
Requires: nbformat
Requires: notebook
Requires: psutil
Requires: requests
BuildRequires : QtPy
BuildRequires : buildreq-distutils3
BuildRequires : nbformat
BuildRequires : notebook
BuildRequires : psutil
BuildRequires : requests

%description
# Spyder notebook plugin
Spyder plugin to use Jupyter notebooks inside Spyder. Currently it supports
basic functionality such as creating new notebooks, opening any notebook in
your filesystem and saving notebooks at any location.

%package license
Summary: license components for the spyder-notebook package.
Group: Default

%description license
license components for the spyder-notebook package.


%package python
Summary: python components for the spyder-notebook package.
Group: Default
Requires: spyder-notebook-python3 = %{version}-%{release}

%description python
python components for the spyder-notebook package.


%package python3
Summary: python3 components for the spyder-notebook package.
Group: Default
Requires: python3-core
Provides: pypi(spyder_notebook)
Requires: pypi(nbformat)
Requires: pypi(notebook)
Requires: pypi(psutil)
Requires: pypi(qtpy)
Requires: pypi(requests)
Requires: pypi(spyder)

%description python3
python3 components for the spyder-notebook package.


%prep
%setup -q -n spyder-notebook-0.2.2
cd %{_builddir}/spyder-notebook-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697972
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spyder-notebook
cp %{_builddir}/spyder-notebook-0.2.2/LICENSE %{buildroot}/usr/share/package-licenses/spyder-notebook/44c99868adf3b229214b4f5c5f924e3a6b7d0eda
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spyder-notebook/44c99868adf3b229214b4f5c5f924e3a6b7d0eda

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
