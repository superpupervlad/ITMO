function Invoke-WindowsFeatureBatchDeployment {
    param (
        [parameter(mandatory)]
        [string[]] $ComputerNames,
        [parameter(mandatory)]
        [string] $ConfigurationFilePath
    )

    $jobs = @()
    foreach($ComputerName in $ComputerNames) {
        $jobs += Start-Job -Command {
            Install-WindowsFeature -ConfigurationFilePath $using:ConfigurationFilePath -ComputerName $using:ComputerName -Restart
        } 
    }

    Receive-Job -Job $jobs -Wait | Select-Object Success, RestartNeeded, ExitCode, FeatureResult
}
