Summary:	Electric Fence C memory debugging library
Summary(de):	Electric Fence C Memory-Debugging-Library
Summary(fr):	Bibliothèque C de débuggage mémoire Electric Fence
Summary(pl):	Biblioteka Electric Fence
Summary(tr):	C için bellek hatasý ayýklama kitaplýðý
Name:		ElectricFence
Version:	2.2.0
Release:	2
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://perens.com/pub/ElectricFence/%{name}-%{version}.tar.gz
Patch0:		ElectricFence-longjmp.patch
patch1:		ElectricFence-shlib.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Electric Fence is a libary that can be used for C programming and debugging.
Package contain shared library libefence which can be loaded by LD_PRELOAD
without relinking debuged program. Package contain also ef shell script
which preloads libefence and runs program passed as parameter.

%description -l de
Electric Fence ist eine Library, die für das Programmieren in C und für
Debugging-Zwecke benutzt werden kann. Sie wird beim Kompilieren gelinkt und
warnt vor möglichen Probleme, etwa vor der Freigabe von nicht existierendem
Speicher und ähnlichem.

%description -l fr
Electric Fence est une bibliothéque utilisée pour la programmation en C et
le débogage. Vous pouvez la lier à la compilation et elle vous avertira des
problèmes éventuels de désallocation de mémoire, etc.

%description -l pl
Electric Fence jest bibliotek± pomocn± podczas programowania w
jêzyku C i "odpluskwianiu".
Pakiet zawiera bibliotekê wspó³dzielon± która mo¿e byæ za³adowana przez
zmienn± LD_PRELOAD w trakcie uruchamiania dowolnego programu dziêki temu nie
potrzeba linkowaæ z t± bibliotek± ¶ledzonego programu. Pakiet zawiera tak¿e
skrypt shellowy ef, któremu mo¿na ³aduje do pamiêci przez LD_PRELOAD
libliotekê libefence i uruchamia program przekazyny do tego skryptu jako
parametr.

%description -l tr
Electric Fence, C'de programlama ve hata ayýklama için kullanýlabilen bir
kitaplýktýr. Derleme esnasýnda programýnýza baðlarsanýz, sizi ortaya
çýkabilecek sorunlar (var olmayan bir bellek parçasýnýn serbest býrakýlmasý
gibi) konusunda uyarýr.

%package static
Summary:	Satatic Electric Fence library
Summary(pl):	Biblioteka statyczna Electric Fence
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze

%description static
Satatic Electric Fence library.

%description -l pl static
Biblioteka statyczna Electric Fence.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man3}

make	BIN_INSTALL_DIR=$RPM_BUILD_ROOT/usr/bin \
	LIB_INSTALL_DIR=$RPM_BUILD_ROOT/usr/lib \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT/usr/man/man3 \
	install

echo .so libefence.3 > $RPM_BUILD_ROOT/usr/man/man3/efence.3

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man3/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) /usr/bin/ef
%attr(755,root,root) /usr/lib/lib*.so.*.*
/usr/man/man3/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Thu Apr 15 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2-2]
- removed "Excludearch: alpha",
- added a patch to properly build the shared library (Maciej W. Ró¿ycki
  <macro@ds2.pg.gda.pl>).

* Mon Apr 12 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2-1]
- added static subpackage; main package contains now shared library which
  can be preloaded for any executable without relinking,
- added static subpackage.

* Sun Apr 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.1-1]
- added Group(pl),
- gzipping %doc.

* Wed Dec 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.0.5-11d]
- build for PLD, 
- major changes.

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- create efence.3 (problem #830)

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- need to use sigsetjmp() and siglongjmp() for proper testing

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use ExcludeArch instead of Exclude

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
