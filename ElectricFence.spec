Summary:	Electric Fence C memory debugging library
Summary(de):	Electric Fence C Memory-Debugging-Library
Summary(fr):	Biblioth�que C de d�buggage m�moire Electric Fence
Summary(pl):	Biblioteka Electric Fence
Summary(tr):	C i�in bellek hatas� ay�klama kitapl���
Name:		ElectricFence
Version:	2.2.2
Release:	2
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://perens.com/pub/ElectricFence/Beta/%{name}-%{version}.tar.gz
Patch0:		ElectricFence-longjmp.patch
Patch1:		ElectricFence-no_bash.spec
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Electric Fence is a libary that can be used for C programming and debugging.
Package contain shared library libefence which can be loaded by LD_PRELOAD
without relinking debuged program. Package contain also ef shell script
which preloads libefence and runs program passed as parameter.

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
Pakiet zawiera bibliotek� wsp�dzielon� kt�ra mo�e by� za�adowana przez
zmienn� LD_PRELOAD w trakcie uruchamiania dowolnego programu dzi�ki temu nie
potrzeba linkowa� z t� bibliotek� �ledzonego programu. Pakiet zawiera tak�e
skrypt shellowy ef, kt�remu mo�na �aduje do pami�ci przez LD_PRELOAD
libliotek� libefence i uruchamia program przekazyny do tego skryptu jako
parametr.

%description -l tr
Electric Fence, C'de programlama ve hata ay�klama i�in kullan�labilen bir
kitapl�kt�r. Derleme esnas�nda program�n�za ba�larsan�z, sizi ortaya
��kabilecek sorunlar (var olmayan bir bellek par�as�n�n serbest b�rak�lmas�
gibi) konusunda uyar�r.

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
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,share/man/man3}

make	BIN_INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir} \
	LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir} \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
	install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README CHANGES

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/ef
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Thu Jun 17 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2.2-2]
- fixed ef.sh script (this is pure sh script),
- added runing /sbin/ldconfig in %post/%postun.

* Fri Jun  4 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2.2-1]
- based on RH spec,
- spec rewrited by PLD team.
