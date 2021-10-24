#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-partitions
Version  : 1.10.4
Release  : 26
URL      : https://cran.r-project.org/src/contrib/partitions_1.10-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/partitions_1.10-4.tar.gz
Summary  : Additive Partitions of Integers
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-partitions-lib = %{version}-%{release}
Requires: R-gmp
Requires: R-mathjaxr
Requires: R-polynom
Requires: R-sets
BuildRequires : R-gmp
BuildRequires : R-mathjaxr
BuildRequires : R-polynom
BuildRequires : R-sets
BuildRequires : buildreq-R

%description
partitions, unequal partitions, and restricted partitions of an
  integer; the three corresponding partition functions are also
  given.  Set partitions and now compositions are included.

%package lib
Summary: lib components for the R-partitions package.
Group: Libraries

%description lib
lib components for the R-partitions package.


%prep
%setup -q -c -n partitions
cd %{_builddir}/partitions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635118728

%install
export SOURCE_DATE_EPOCH=1635118728
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library partitions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library partitions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library partitions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc partitions || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/partitions/CITATION
/usr/lib64/R/library/partitions/DESCRIPTION
/usr/lib64/R/library/partitions/INDEX
/usr/lib64/R/library/partitions/Meta/Rd.rds
/usr/lib64/R/library/partitions/Meta/features.rds
/usr/lib64/R/library/partitions/Meta/hsearch.rds
/usr/lib64/R/library/partitions/Meta/links.rds
/usr/lib64/R/library/partitions/Meta/nsInfo.rds
/usr/lib64/R/library/partitions/Meta/package.rds
/usr/lib64/R/library/partitions/Meta/vignette.rds
/usr/lib64/R/library/partitions/NAMESPACE
/usr/lib64/R/library/partitions/R/partitions
/usr/lib64/R/library/partitions/R/partitions.rdb
/usr/lib64/R/library/partitions/R/partitions.rdx
/usr/lib64/R/library/partitions/doc/index.html
/usr/lib64/R/library/partitions/doc/partitionspaper.R
/usr/lib64/R/library/partitions/doc/partitionspaper.Rnw
/usr/lib64/R/library/partitions/doc/partitionspaper.pdf
/usr/lib64/R/library/partitions/doc/scrabble.R
/usr/lib64/R/library/partitions/doc/scrabble.Rnw
/usr/lib64/R/library/partitions/doc/scrabble.pdf
/usr/lib64/R/library/partitions/doc/setpartitions.R
/usr/lib64/R/library/partitions/doc/setpartitions.Rnw
/usr/lib64/R/library/partitions/doc/setpartitions.pdf
/usr/lib64/R/library/partitions/help/AnIndex
/usr/lib64/R/library/partitions/help/aliases.rds
/usr/lib64/R/library/partitions/help/figures/partitions.png
/usr/lib64/R/library/partitions/help/partitions.rdb
/usr/lib64/R/library/partitions/help/partitions.rdx
/usr/lib64/R/library/partitions/help/paths.rds
/usr/lib64/R/library/partitions/html/00Index.html
/usr/lib64/R/library/partitions/html/R.css
/usr/lib64/R/library/partitions/tests/testthat.R
/usr/lib64/R/library/partitions/tests/testthat/test_aaa.R
/usr/lib64/R/library/partitions/tests/testthat/test_aab.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/partitions/libs/partitions.so
/usr/lib64/R/library/partitions/libs/partitions.so.avx2
/usr/lib64/R/library/partitions/libs/partitions.so.avx512
