Summary:	JACK and ALSA Perceptual Analyser
Summary(pl.UTF-8):	Analizator percepcyjny JACK i ALSA
Name:		japa
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	43287acd2511c6f9aeff7951b6e07d79
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/index.html
BuildRequires:	clthreads-devel >= 2.4.0
BuildRequires:	clxclient-devel >= 3.9.0
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	zita-alsa-pcmi-devel >= 0.3.0
Requires:	clthreads >= 2.4.0
Requires:	clxclient >= 3.9.0
Requires:	zita-alsa-pcmi >= 0.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Japa (JACK and ALSA Perceptual Analyser), is a 'perceptual' or
'psychoacoustic' audio spectrum analyser. In contrast to JAAA, this is
more an acoustical or musical tool than a purely technical one.
Possible uses include spectrum monitoring while mixing or mastering,
evaluation of ambient noise, and (using pink noise), equalisation of
PA systems.

%description -l pl.UTF-8
Japa (JACK and ALSA Perceptual Analyser) to "percepcyjny" albo
"psychoakustyczny" analizator widma dźwięku. W przeciwieństwie do JAAA
to jest narzędzie bardziej akustyczne albo muzyczne niż techniczne.
Możliwe przypadki użycia obejmują monitorowanie widma przy miksowaniu
lub masteringu, szacowanie szumu otoczenia lub (przy użyciu różowego
szumu) dostrajanie systemów PA.

%prep
%setup -q
%patch0 -p1

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/japa
