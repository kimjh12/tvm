Name:       tvm-runtime
Summary:    TVM Runtime Library
Version:    0.7.0
Release:    0

# ==========================================================
License:    Apache-2.0 
# ==========================================================

Group:      Machine Learning/ML Framework
Source0:    %{name}-%{version}.tar.gz
Source1001: %{name}.manifest

# ==========================================================
# BuildRequires
# specifies build-time dependencies for the package
# ==========================================================
BuildRequires:  cmake 

%description
%{name} version %{version}

%package devel
Summary:    develelopment package
Requires:   tvm-runtime = %{version}-%{release}
%description devel
development package for tvm

%prep
%setup -q
cp %{SOURCE1001} .


# ==========================================================
# build section
# how to actually build the software we are packaging
# ==========================================================
%build
mkdir -p build
cp cmake/config.cmake build
pushd build
%{cmake} .. 
%{__make} runtime %{?_smp_mflags}
popd


# ==========================================================
# install section
# how to actually build the software we are packaging
# ==========================================================
%install
pushd build
%{make_install}
popd


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

# ==========================================================
# files section
# The list of files that will be installed in the end
# user???s system.
# ==========================================================
%files
%manifest %{name}.manifest
%{_libdir}/*.so

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/tvm_runtime.pc
