Summary:	A debugger which detects memory allocation violations
Summary(cs):	Nástroj pro odhalování chyb pøi alokaci dynamické pamìti
Summary(da):	En afluser som finder problemer ved hukommelsesallokering
Summary(de):	Debugger zum Erkennen von Speicherzugriffsverletzungen
Summary(es):	Electric Fence biblioteca de depuración de memoria en C
Summary(fr):	Bibliothèque C de débuggage mémoire Electric Fence
Summary(id):	Debugger untuk menditeksi memory allocation violations
Summary(is):	Aflúsunartól sem finnur villur í minnismeðhöndlun
Summary(it):	Debugger che rileva le violazioni dell'allocazione di memoria
Summary(ja):	¥á¥â¥ê³ä¤êÅö¤Æ¤Î¿¯Î¬¤ò¸¡½Ð¤¹¤ë¥Ç¥Ð¥Ã¥¬
Summary(nb):	Et avlusingsprogram som finner overtramp ved minneallokering
Summary(pl):	Biblioteka do wykrywania b³êdów alokacji pamiêci
Summary(pt):	Um depurador que detecta violações à memória alocada
Summary(pt_BR):	Electric Fence biblioteca de depuração de memória em C
Summary(ru):	ïÔÌÁÄÞÉË, ×ÙÑ×ÌÑÀÝÉÊ ÏÛÉÂËÉ × ÒÁÓÐÒÅÄÅÌÅÎÉÉ ÐÁÍÑÔÉ
Summary(sk):	Debugger pre vyhµadávanie chybných prístupov k alokovanej pamäti
Summary(sl):	Razhro¹èevalnik, ki najde prekoraèitve dodeljenega pomnilnika
Summary(sv):	Ett avlusningsprogram som upptäcker minnesallokeringsfel
Summary(tr):	C için bellek hatasý ayýklama kitaplýðý
Summary(zh_CN):	Ò»ÖÖµ÷ÊÔÆ÷ÓÃÓÚ¼ì²âÄÚ´æ·ÖÅä´íÎó
Name:		ElectricFence
Version:	2.2.2
Release:	13
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.perens.com/pub/ElectricFence/Beta/%{name}-%{version}.tar.gz
# Source0-md5:	56a3cbfdbf65f916988787c789c63e80
Patch0:		%{name}-longjmp.patch
Patch1:		%{name}-no_bash.spec
Patch2:		%{name}-va_arg.patch
Patch3:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libefence0

%description
If you know what malloc() violations are, you'll be interested in
ElectricFence. ElectricFence is a tool which can be used for C
programming and debugging. It uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by free().
ElectricFence will then stop the program on the first instruction that
caused a bounds violation and you can use your favorite debugger to
display the offending statement.

%description -l de
Wenn Sie wissen, was malloc()-Verletzungen sind, sind Sie
wahrscheinlich an ElectricFence interessiert. ElectricFence ist ein
Tool, das zur C- Programmierung und zum Debugging benutzt werden kann.
Es benutzt virtuelle Speicherhardware, um zu erkennen, wenn Software
malloc()-Buffergrenzen übersteigt, und wenn Speicher mit free()
freigegeben wird. ElectricFence beendet das Programm bei der
Instruktion, die die Speicherverletzung ausgelöst hat, und Sie können
Ihren Lieblingsdebugger benutzen, um den Befehl anzuzeigen.

%description -l es
ElectricFence es una herramienta que puede usarse para programación y
depuración en lenguaje C. A través del uso del hardware de memoria
virtual del sistema, detecta accesos que sobrepasan los límites de la
memoria asignada con malloc(), o acceso a la memoria liberada por
free(). En esas situaciones, ElectricFence interrumpe la ejecución del
programa en la primera instrucción que causó la violación, y puede
usarse un debugger para verificar la causa del problema.

%description -l fr
Electric Fence est une bibliothéque utilisée pour la programmation en
C et le débogage. Vous pouvez la lier à la compilation et elle vous
avertira des problèmes éventuels de désallocation de mémoire, etc.

%description -l pl
Electric Fence jest bibliotek± pomocn± podczas programowania w jêzyku
C i "odpluskwiania". Pakiet zawiera bibliotekê wspó³dzielon±, która
mo¿e byæ za³adowana przez zmienn± LD_PRELOAD w trakcie uruchamiania
dowolnego programu dziêki temu nie potrzeba konsolidowaæ z t±
bibliotek± ¶ledzonego programu. Pakiet zawiera tak¿e skrypt pow³oki
ef, który ³aduje do pamiêci przez LD_PRELOAD bibliotekê libefence i
uruchamia program przekazany do tego skryptu jako parametr.

%description -l pt_BR
ElectricFence é uma ferramenta que pode ser usada com programação e
depuracao em linguagem C. Através do uso do hardware de memoria
virtual do sistema, o ElectricFence detecta acessos além dos limites
da memória alocada com malloc(), ou acesso a memória liberada por
free(). Nessas situações, o ElectricFence interrompe a execução do
programa na primeira instrução que causou a violação, e um debugger
pode ser usado para verificar a causa do problema.

%description -l tr
Electric Fence, C'de programlama ve hata ayýklama için kullanýlabilen
bir kitaplýktýr. Derleme esnasýnda programýnýza baðlarsanýz, sizi
ortaya çýkabilecek sorunlar (var olmayan bir bellek parçasýnýn serbest
býrakýlmasý gibi) konusunda uyarýr.

%package static
Summary:	Static Electric Fence library
Summary(pl):	Biblioteka statyczna Electric Fence
Group:		Development/Debuggers
Obsoletes:	libefence0-devel

%description static
Static Electric Fence library.

%description static -l pl
Biblioteka statyczna Electric Fence.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -DUSE_SEMAPHORE"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/ef
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
