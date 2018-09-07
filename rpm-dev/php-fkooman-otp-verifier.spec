%global commit0 2f5c4770a76cf1f4c913a35977108314b3af9ade

Name:           php-fkooman-otp-verifier
Version:        0.2.0
Release:        6%{?dist}
Summary:        OTP Verification Library

License:        MIT
URL:            https://git.tuxed.net/fkooman/php-otp-verifier
Source0:        https://git.tuxed.net/fkooman/php-otp-verifier/snapshot/php-otp-verifier-%{commit0}.tar.xz

BuildArch:      noarch

#        "php": ">= 5.4",
BuildRequires:  php(language) >= 5.4.0
#        "ext-date": "*",
#        "ext-hash": "*",
#        "ext-pdo": "*",
#        "ext-spl": "*",
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pdo
BuildRequires:  php-spl
#        "paragonie/constant_time_encoding": "^1|^2",
#        "paragonie/random_compat": ">=1",
#        "symfony/polyfill-php56": "^1"
BuildRequires:  php-composer(paragonie/constant_time_encoding)
%if 0%{?fedora} < 28 && 0%{?rhel} < 8
BuildRequires:  php-composer(paragonie/random_compat)
BuildRequires:  php-composer(symfony/polyfill-php56)
%endif
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  %{_bindir}/phpab

%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
BuildRequires:  phpunit7
%global phpunit %{_bindir}/phpunit7
%else
BuildRequires:  phpunit
%global phpunit %{_bindir}/phpunit
%endif

#        "php": ">= 5.4",
Requires:  php(language) >= 5.4.0
#        "ext-date": "*",
#        "ext-hash": "*",
#        "ext-pdo": "*",
#        "ext-spl": "*",
Requires:  php-date
Requires:  php-hash
Requires:  php-pdo
Requires:  php-spl
#        "paragonie/constant_time_encoding": "^1|^2",
#        "paragonie/random_compat": ">=1",
#        "symfony/polyfill-php56": "^1"
Requires:  php-composer(paragonie/constant_time_encoding)
%if 0%{?fedora} < 28 && 0%{?rhel} < 8
Requires:  php-composer(paragonie/random_compat)
Requires:  php-composer(symfony/polyfill-php56)
%endif

Provides:       php-composer(fkooman/otp-verifier) = %{version}

%description
OTP Verification Library

%prep
%autosetup -n php-otp-verifier-%{commit0}

%build
%{_bindir}/phpab -t fedora -o src/autoload.php src
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
cat <<'AUTOLOAD' | tee -a src/autoload.php
require_once '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php';
AUTOLOAD
%else
cat <<'AUTOLOAD' | tee -a src/autoload.php
require_once '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php';
require_once '%{_datadir}/php/random_compat/autoload.php';
require_once '%{_datadir}/php/Symfony/Polyfill/autoload.php';
AUTOLOAD
%endif

%install
mkdir -p %{buildroot}%{_datadir}/php/fkooman/Otp
cp -pr src/* %{buildroot}%{_datadir}/php/fkooman/Otp

%check
%{_bindir}/phpab -o tests/autoload.php tests
cat <<'AUTOLOAD' | tee -a tests/autoload.php
require_once 'src/autoload.php';
AUTOLOAD

%{phpunit} tests --verbose --bootstrap=tests/autoload.php

%files
%license LICENSE
%doc composer.json CHANGES.md README.md
%dir %{_datadir}/php/fkooman
%{_datadir}/php/fkooman/Otp

%changelog
* Fri Sep 07 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-6
- rebuilt

* Fri Sep 07 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-5
- rebuilt

* Thu Jul 26 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-4
- use PHPUnit 7 on Fedora >= 27, EL >= 8

* Mon Jul 23 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-3
- add missing BR

* Mon Jul 23 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-2
- use fedora phpab template

* Fri Jul 20 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-1
- update to 0.2.0

* Mon Jul 16 2018 François Kooman <fkooman@tuxed.net> - 0.1.1-1
- update to 0.1.1

* Tue Jul 10 2018 François Kooman <fkooman@tuxed.net> - 0.1.0-0.1
- initial package
