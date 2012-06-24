Summary:	Electric Fence C memory debugging library
Summary(de):	Electric Fence C Memory-Debugging-Library
Summary(fr):	Biblioth�que C de d�buggage m�moire Electric Fence
Summary(pl):	Biblioteka Electric Fence
Summary(tr):	C i�in bellek hatas� ay�klama kitapl���
Name:		ElectricFence
Version:	2.1
Release:	1
Excludearch:	alpha
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://perens.com/pub/ElectricFence/%{name}-%{version}.tar.gz
Patch0:		ElectricFence-glibc.patch
Patch1:		ElectricFence-longjmp.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Electric Fence is a libary that can be used for C programming and debugging.
You link it in at compile time and it will warn you of possible problems
such as free'ing memory that doesn't exist, etc.

%description -l de
Electric Fence ist eine Library, die f�r das Programmieren in C und f�r
Debugging-Zwecke benutzt werden kann. Sie wird beim Kompilieren gelinkt und
warnt vor m�glichen Probleme, etwa vor der Freigabe von nicht existierendem
Speicher und �hnlichem.

%description -l fr
Electric Fence est une biblioth�que utilis�e pour la programmation en C et
le d�bogage. Vous pouvez la lier � la compilation et elle vous avertira des
probl�mes �ventuels de d�sallocation de m�moire, etc.

%description -l pl
Electric Fence jest bibliotek� pomocn� podczas programowania w
j�zyku C i "odpluskwianiu".

%description -l tr
Electric Fence, C'de programlama ve hata ay�klama i�in kullan�labilen bir
kitapl�kt�r. Derleme esnas�nda program�n�za ba�larsan�z, sizi ortaya
��kabilecek sorunlar (var olmayan bir bellek par�as�n�n serbest b�rak�lmas�
gibi) konusunda uyar�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,man/man3}

make	LIB_INSTALL_DIR=$RPM_BUILD_ROOT/usr/lib \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT/usr/man/man3 \
	install

echo .so libefence.3 > $RPM_BUILD_ROOT/usr/man/man3/efence.3

gzip -9nf $RPM_BUILD_ROOT/usr/man/man3/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
/usr/lib/lib*.a
/usr/man/man3/*

%changelog
* Sun Apr 11 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.1-1]
- added Group(pl),
- gzipping $doc.

* Wed Dec 30 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
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
