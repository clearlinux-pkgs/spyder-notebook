#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spyder-notebook
Version  : 0.3.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/81/ac/f15a79e7d123b29919b5f36593c30e157555957e21e62fb142fbb290357d/spyder-notebook-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/ac/f15a79e7d123b29919b5f36593c30e157555957e21e62fb142fbb290357d/spyder-notebook-0.3.0.tar.gz
Summary  : Jupyter notebook integration with Spyder
Group    : Development/Tools
License  : MIT
Requires: spyder-notebook-python = %{version}-%{release}
Requires: spyder-notebook-python3 = %{version}-%{release}
Requires: Jinja2
Requires: QtPy
Requires: jupyter_core
Requires: nbformat
Requires: notebook
Requires: requests
Requires: traitlets
BuildRequires : Jinja2
BuildRequires : QtPy
BuildRequires : buildreq-distutils3
BuildRequires : nbformat
BuildRequires : notebook
BuildRequires : requests
BuildRequires : traitlets

%description
# Spyder notebook plugin
Spyder plugin to use Jupyter notebooks inside Spyder. Currently it supports
basic functionality such as creating new notebooks, opening any notebook in
your filesystem and saving notebooks at any location.

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
Requires: pypi(jinja2)
Requires: pypi(jupyter_core)
Requires: pypi(nbformat)
Requires: pypi(notebook)
Requires: pypi(qdarkstyle)
Requires: pypi(qtpy)
Requires: pypi(requests)
Requires: pypi(spyder)
Requires: pypi(traitlets)

%description python3
python3 components for the spyder-notebook package.


%prep
%setup -q -n spyder-notebook-0.3.0
cd %{_builddir}/spyder-notebook-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596130696
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
