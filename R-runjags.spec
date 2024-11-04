#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: 1ab68ca
#
Name     : R-runjags
Version  : 2.2.2.4
Release  : 47
URL      : https://cran.r-project.org/src/contrib/runjags_2.2.2-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/runjags_2.2.2-4.tar.gz
Summary  : Interface Utilities, Model Templates, Parallel Computing Methods
Group    : Development/Tools
License  : GPL-2.0
Requires: R-runjags-lib = %{version}-%{release}
Requires: R-runjags-license = %{version}-%{release}
Requires: R-coda
BuildRequires : JAGS-dev
BuildRequires : R-coda
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Just Another Gibbs Sampler (JAGS), facilitating the use of parallel
    (or distributed) processors for multiple chains, automated control
    of convergence and sample length diagnostics, and evaluation of the
    performance of a model using drop-k validation or against simulated
    data. Template model specifications can be generated using a standard
    lme4-style formula interface to assist users less familiar with the
    BUGS syntax.  A JAGS extension module provides additional distributions
    including the Pareto family of distributions, the DuMouchel prior and
    the half-Cauchy prior.

%package lib
Summary: lib components for the R-runjags package.
Group: Libraries
Requires: R-runjags-license = %{version}-%{release}

%description lib
lib components for the R-runjags package.


%package license
Summary: license components for the R-runjags package.
Group: Default

%description license
license components for the R-runjags package.


%prep
%setup -q -n runjags
pushd ..
cp -a runjags buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710176415

%install
export SOURCE_DATE_EPOCH=1710176415
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-runjags
cp %{_builddir}/runjags/COPYING %{buildroot}/usr/share/package-licenses/R-runjags/dfac199a7539a404407098a2541b9482279f690d || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/runjags/CITATION
/usr/lib64/R/library/runjags/DESCRIPTION
/usr/lib64/R/library/runjags/INDEX
/usr/lib64/R/library/runjags/Meta/Rd.rds
/usr/lib64/R/library/runjags/Meta/features.rds
/usr/lib64/R/library/runjags/Meta/hsearch.rds
/usr/lib64/R/library/runjags/Meta/links.rds
/usr/lib64/R/library/runjags/Meta/nsInfo.rds
/usr/lib64/R/library/runjags/Meta/package.rds
/usr/lib64/R/library/runjags/Meta/vignette.rds
/usr/lib64/R/library/runjags/NAMESPACE
/usr/lib64/R/library/runjags/R/runjags
/usr/lib64/R/library/runjags/R/runjags.rdb
/usr/lib64/R/library/runjags/R/runjags.rdx
/usr/lib64/R/library/runjags/WORDLIST
/usr/lib64/R/library/runjags/doc/UserGuide.Rtex
/usr/lib64/R/library/runjags/doc/UserGuide.pdf
/usr/lib64/R/library/runjags/doc/index.html
/usr/lib64/R/library/runjags/doc/quickjags.R
/usr/lib64/R/library/runjags/doc/quickjags.Rmd
/usr/lib64/R/library/runjags/doc/quickjags.html
/usr/lib64/R/library/runjags/help/AnIndex
/usr/lib64/R/library/runjags/help/aliases.rds
/usr/lib64/R/library/runjags/help/paths.rds
/usr/lib64/R/library/runjags/help/runjags.rdb
/usr/lib64/R/library/runjags/help/runjags.rdx
/usr/lib64/R/library/runjags/html/00Index.html
/usr/lib64/R/library/runjags/html/R.css
/usr/lib64/R/library/runjags/tests/check_huiwalter.R
/usr/lib64/R/library/runjags/tests/checkinputs.R
/usr/lib64/R/library/runjags/tests/checkmethods.R
/usr/lib64/R/library/runjags/tests/checkmodule.R
/usr/lib64/R/library/runjags/tests/checkstudy.R
/usr/lib64/R/library/runjags/tests/moduletargets.Rsave
/usr/lib64/R/library/runjags/tests/spelling.R
/usr/lib64/R/library/runjags/tests/testthat.R
/usr/lib64/R/library/runjags/tests/testthat/test-basic_example.R
/usr/lib64/R/library/runjags/xgrid/beep.bat

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/runjags/libs/runjags.so
/usr/lib64/R/library/runjags/libs/runjags.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-runjags/dfac199a7539a404407098a2541b9482279f690d
