Summary:	A debugger which detects memory allocation violations
Summary(de):	Debugger zum Erkennen von Speicherzugriffsverletzungen
Summary(es):	Electric Fence biblioteca de depuraci�n de memoria en C
Summary(fr):	Biblioth�que C de d�buggage m�moire Electric Fence
Summary(pl):	Biblioteka do wykrywania b�ed�w alokacji pami�ci
Summary(pt_BR):	Electric Fence biblioteca de depura��o de mem�ria em C
Summary(tr):	C i�in bellek hatas� ay�klama kitapl���
Name:		ElectricFence
Version:	2.2.2
Release:	3
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://perens.com/pub/ElectricFence/Beta/%{name}-%{version}.tar.gz
Patch0:		ElectricFence-longjmp.patch
Patch1:		ElectricFence-no_bash.spec
BuildRoot:	/tmp/%{name}-%{version}-root

%description
If you know what malloc() violations are, you'll be interested in
ElectricFence. ElectricFence is a tool which can be used for C programming
and debugging. It uses the virtual memory hardware of your system to detect
when software overruns malloc() buffer boundaries, and/or to detect any
accesses of memory released by free(). ElectricFence will then stop the
program on the first instruction that caused a bounds violation and you can
use your favorite debugger to display the offending statement.

This package will install ElectricFence, which you can use if you're
searching for a debugger to find malloc() violations.

%description -l de
Wenn Sie wissen, was malloc()-Verletzungen sind, sind Sie wahrscheinlich an
ElectricFence interessiert. ElectricFence ist ein Tool, das zur C-
Programmierung und zum Debugging benutzt werden kann. Es benutzt virtuelle
Speicherhardware, um zu erkennen, wenn Software malloc()-Buffergrenzen
�bersteigt, und wenn Speicher mit free() freigegeben wird. ElectricFence
beendet das Programm bei der Instruktion, die die Speicherverletzung
ausgel�st hat, und Sie k�nnen Ihren Lieblingsdebugger benutzen, um den
Befehl anzuzeigen.

%description -l es
Electric Fence es una biblioteca que puede ser usada para programaci�n y
depuraci�n en C. Tu lo "linkas" en tiempo de compilaci�n y te avisar� sobre
posibles problemas, como liberaci�n de memoria no alocada, etc.

%description -l fr
Electric Fence est une biblioth�que utilis�e pour la programmation en C et
le d�bogage. Vous pouvez la lier � la compilation et elle vous avertira des
probl�mes �ventuels de d�sallocation de m�moire, etc.

%description -l pl
Electric Fence jest bibliotek� pomocn� podczas programowania w
j�zyku C i "odpluskwianiu".
Pakiet zawiera bibliotek� wsp�dzielon�, kt�ra mo�e by� za�adowana przez
zmienn� LD_PRELOAD w trakcie uruchamiania dowolnego programu dzi�ki temu nie
potrzeba linkowa� z t� bibliotek� �ledzonego programu. Pakiet zawiera tak�e
skrypt pow�oki ef, kt�ry �aduje do pami�ci przez LD_PRELOAD bibliotek�
libefence i uruchamia program przekazyny do tego skryptu jako parametr.

%description -l pt_BR
Electric Fence � uma biblioteca que pode ser usada para programa��o e
depura��o em C. Voc� o "linka" em tempo de compila��o e ele o avisar� sobre
poss�veis problemas como libera��o de mem�ria n�o alocada, etc.

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
