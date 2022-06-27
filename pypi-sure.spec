#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sure
Version  : 2.0.0
Release  : 77
URL      : https://files.pythonhosted.org/packages/c7/ee/043531858afab5f312ca02867de51189c0c1dd76ba652f1d95ffa13d07f7/sure-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c7/ee/043531858afab5f312ca02867de51189c0c1dd76ba652f1d95ffa13d07f7/sure-2.0.0.tar.gz
Summary  : utility belt for automated testing in python for python
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: pypi-sure-bin = %{version}-%{release}
Requires: pypi-sure-license = %{version}-%{release}
Requires: pypi-sure-python = %{version}-%{release}
Requires: pypi-sure-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(mock)
BuildRequires : pypi(nose)
BuildRequires : pypi(py)
BuildRequires : pypi(six)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
sure
====
.. image:: https://img.shields.io/pypi/dm/sure
:target: https://pypi.org/project/sure

%package bin
Summary: bin components for the pypi-sure package.
Group: Binaries
Requires: pypi-sure-license = %{version}-%{release}

%description bin
bin components for the pypi-sure package.


%package license
Summary: license components for the pypi-sure package.
Group: Default

%description license
license components for the pypi-sure package.


%package python
Summary: python components for the pypi-sure package.
Group: Default
Requires: pypi-sure-python3 = %{version}-%{release}

%description python
python components for the pypi-sure package.


%package python3
Summary: python3 components for the pypi-sure package.
Group: Default
Requires: python3-core
Provides: pypi(sure)
Requires: pypi(mock)
Requires: pypi(six)

%description python3
python3 components for the pypi-sure package.


%prep
%setup -q -n sure-2.0.0
cd %{_builddir}/sure-2.0.0
pushd ..
cp -a sure-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656369399
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sure
cp %{_builddir}/sure-2.0.0/COPYING %{buildroot}/usr/share/package-licenses/pypi-sure/3253d5140ac4cae1fafff57226a76d45d79429f0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sure

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sure/3253d5140ac4cae1fafff57226a76d45d79429f0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
