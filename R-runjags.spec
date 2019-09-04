#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-runjags
Version  : 2.0.4.4
Release  : 12
URL      : https://cran.r-project.org/src/contrib/runjags_2.0.4-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/runjags_2.0.4-4.tar.gz
Summary  : Interface Utilities, Model Templates, Parallel Computing Methods
Group    : Development/Tools
License  : GPL-2.0
Requires: R-runjags-lib = %{version}-%{release}
Requires: R-coda
BuildRequires : JAGS-dev
BuildRequires : R-coda
BuildRequires : buildreq-R

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

%description lib
lib components for the R-runjags package.


%prep
%setup -q -c -n runjags

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567569394

%install
export SOURCE_DATE_EPOCH=1567569394
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library runjags
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library runjags
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library runjags
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

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
/usr/lib64/R/library/runjags/tests/checkinputs.R
/usr/lib64/R/library/runjags/tests/checkmethods.R
/usr/lib64/R/library/runjags/tests/checkmodule.R
/usr/lib64/R/library/runjags/tests/checkstudy.R
/usr/lib64/R/library/runjags/tests/moduletargets.Rsave
/usr/lib64/R/library/runjags/xgrid/beep.bat
/usr/lib64/R/library/runjags/xgrid/mgrid.sh

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/runjags/libs/runjags.so
/usr/lib64/R/library/runjags/libs/runjags.so.avx2
